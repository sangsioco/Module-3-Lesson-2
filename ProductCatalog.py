# Catalog Merging
def merge_catalogs(*catalogs):
    combined_catalog = []
    for catalog in catalogs:
        combined_catalog.extend(catalog)
    return tuple(combined_catalog)

catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))


combined_catalog = merge_catalogs(catalog1, catalog2)

print(combined_catalog)
