select
    id,
    software_name,
    vendor,
    license_type,
    purchase_date,
    expiration_date,
    cost,
    status,
    assigned_to,
    department
from main.softasset_sam_csv_final.softasset_raw
where status is not null
    and id is not null
