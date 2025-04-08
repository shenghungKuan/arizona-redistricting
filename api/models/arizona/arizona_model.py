import geopandas as gpd
import maup
from maup import smart_repair

maup.progress.enabled = True
import warnings
warnings.filterwarnings('ignore')

def get_clean_data():
    population_df = gpd.read_file("../../data/arizona/az_pl2020_b/az_pl2020_p2_b.shp")
    vap_df = gpd.read_file("../../data/arizona/az_pl2020_b/az_pl2020_p4_b.shp")
    vest20_df = gpd.read_file("../../data/arizona/az_vest_20/az_vest_20.shp")
    county_df = gpd.read_file("../../data/arizona/az_pl2020_cnty/az_pl2020_cnty.shp")
    sen_df = gpd.read_file("../../data/arizona/az_pl2020_sldu/az_pl2020_sldu.shp")
    sen_df['SLDUST20'] = sen_df['SLDUST20'].astype(str).str.lstrip('0').astype(int)
    district_col_name = "SLDUST20"
    population_df = population_df.to_crs(population_df.estimate_utm_crs())
    vap_df = vap_df.to_crs(vap_df.estimate_utm_crs())
    county_df = county_df.to_crs(county_df.estimate_utm_crs())
    sen_df = sen_df.to_crs(sen_df.estimate_utm_crs())
    vest20_df = vest20_df.to_crs(vest20_df.estimate_utm_crs())
    maup.doctor(population_df)
    maup.doctor(vap_df)
    maup.doctor(county_df)
    maup.doctor(sen_df)
    maup.doctor(vest20_df)
    final_df = smart_repair(vest20_df, nest_within_regions=county_df)
    final_df = smart_repair(final_df, min_rook_length=30)
    maup.doctor(final_df)

    # %%
    # print("Number of Senate Seats \n", sen_df.shape)
    # print("Population Age \n", population_df.columns)
    # print("Voting Age \n", vap_df.columns)
    # print("Presidential Results \n", vest20_df.columns)
    # print("County Lines \n", county_df.columns)
    print("Senate Columns \n", sen_df.columns.values.tolist())

    return  {
        # "population_df": population_df,
        # "vap_df": vap_df,
        # "vest20_df": vest20_df,
        # "county_df": county_df,
        "sen_df": sen_df,
    }

get_clean_data()