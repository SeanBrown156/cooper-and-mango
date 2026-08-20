"""Checks for the smallest real Stage 1 content dataset."""

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
LIFECYCLE_STATES = {"idea", "draft", "review", "approved", "exported", "retired"}
ID_PREFIXES = {
    "actors": "actor",
    "abilities": "skill",
    "items": "item",
    "enemies": "enemy",
    "encounters": "encounter",
    "dialogue": "dialogue",
}


def load_records(table):
    records = []
    for path in sorted((DATA / table).glob("*.json")):
        with path.open(encoding="utf-8") as stream:
            record = json.load(stream)
        records.append((path, record))
    return records


class Stage1DataTest(unittest.TestCase):
    def test_expected_stage1_records_exist(self):
        expected = {
            "actors": {"actor_mango", "actor_cooper"},
            "abilities": {"skill_judgemental_stare", "skill_brave_bark"},
            "items": {"item_cat_kibble"},
            "enemies": {"enemy_dust_bunny"},
            "encounters": {"encounter_tutorial_dust_bunny"},
            "dialogue": {"dialogue_mango_meets_cooper"},
        }

        for table, ids in expected.items():
            with self.subTest(table=table):
                self.assertEqual({record["id"] for _, record in load_records(table)}, ids)

    def test_records_have_schema_fields_and_stable_file_ids(self):
        for table in ("actors", "abilities", "items", "enemies", "encounters", "dialogue"):
            for path, record in load_records(table):
                with self.subTest(path=path):
                    self.assertRegex(record["id"], rf"^{ID_PREFIXES[table]}_[a-z0-9_]+$")
                    self.assertEqual(path.stem, record["id"])
                    self.assertTrue(record["name"])
                    self.assertTrue(record["description"])
                    self.assertIn(record["content_status"], LIFECYCLE_STATES)

    def test_stage1_relationships_resolve(self):
        actors = {record["id"]: record for _, record in load_records("actors")}
        abilities = {record["id"]: record for _, record in load_records("abilities")}
        items = {record["id"] for _, record in load_records("items")}
        enemies = {record["id"] for _, record in load_records("enemies")}
        dialogue = load_records("dialogue")[0][1]
        encounter = load_records("encounters")[0][1]

        self.assertEqual({actor["id"] for actor in actors.values()}, {"actor_mango", "actor_cooper"})
        for actor in actors.values():
            self.assertEqual(len(actor["abilities"]), 1)
            ability_id = actor["abilities"][0]
            self.assertIn(ability_id, abilities)
            self.assertEqual(abilities[ability_id]["user_id"], actor["id"])

        self.assertEqual(encounter["party"], ["actor_mango", "actor_cooper"])
        self.assertEqual(encounter["enemies"], [{"enemy_id": "enemy_dust_bunny", "count": 1}])
        self.assertIn("enemy_dust_bunny", enemies)
        self.assertIn("item_cat_kibble", items)

        nodes = dialogue["nodes"]
        self.assertGreaterEqual(len(nodes), 2)
        node_ids = {node["id"] for node in nodes}
        for node in nodes:
            if "next_id" in node:
                self.assertIn(node["next_id"], node_ids)
        self.assertEqual(nodes[-1].get("next_id"), None)


if __name__ == "__main__":
    unittest.main()
