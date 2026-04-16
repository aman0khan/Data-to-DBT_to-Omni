/**
 * TypeScript types for the softasset_dbt project.
 *
 * These types correspond to the dbt models defined in dbt_project.yml,
 * targeting catalog 'main' and schema 'softasset_sam_csv_final'.
 */

/** Represents a row from the raw_softasset dbt model. */
export interface RawSoftasset {
  id: number;
  asset_name: string;
  asset_type: string | null;
  version: string | null;
  license_type: string | null;
  vendor: string | null;
  purchase_date: string | null;
  expiry_date: string | null;
  cost: number | null;
  status: string | null;
  assigned_to: string | null;
  department: string | null;
  notes: string | null;
}

/** dbt project configuration matching dbt_project.yml */
export interface DbtProjectConfig {
  name: "softasset_dbt";
  version: "1.0.0";
  config_version: 2;
  profile: "default";
  model_paths: string[];
  analysis_paths: string[];
  test_paths: string[];
  seed_paths: string[];
  macro_paths: string[];
  snapshot_paths: string[];
  target_path: string;
  clean_targets: string[];
}

/** dbt model configuration for softasset_dbt models */
export interface DbtModelConfig {
  catalog: "main";
  schema: "softasset_sam_csv_final";
  materialized: "table";
}

/** Project-level metadata constants matching dbt_project.yml */
export const DBT_PROJECT_NAME = "softasset_dbt" as const;
export const DBT_PROJECT_VERSION = "1.0.0" as const;
export const DBT_CATALOG = "main" as const;
export const DBT_SCHEMA = "softasset_sam_csv_final" as const;
export const DBT_MATERIALIZED = "table" as const;
