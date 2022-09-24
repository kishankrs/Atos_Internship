csv_f = 'breast-cancer.csv'
model_pkl = 'sav_model.pkl'
features_init = ['concave points_worst', 'perimeter_worst', 'concave points_mean', 'radius_worst', 'perimeter_mean', 'area_worst', 'radius_mean', 'area_mean', 'concavity_mean', 'concavity_worst', 'compactness_mean', 'compactness_worst', 'radius_se', 'perimeter_se', 'area_se',
                 'texture_worst', 'smoothness_worst', 'symmetry_worst', 'texture_mean', 'concave points_se', 'smoothness_mean', 'symmetry_mean', 'fractal_dimension_worst', 'compactness_se', 'concavity_se', 'fractal_dimension_se', 'symmetry_se', 'texture_se', 'fractal_dimension_mean', 'smoothness_se']
features = ["radius_mean", "texture_mean", "perimeter_mean", "area_mean",
            "compactness_mean", "concavity_mean", "concave points_mean",
            "symmetry_mean", "radius_se", "perimeter_se", "area_se",
            "smoothness_se", "compactness_se", "concave points_se", "symmetry_se",
            "fractal_dimension_se", "radius_worst", "texture_worst",
            "perimeter_worst", "area_worst", "smoothness_worst", "concavity_worst",
            "concave points_worst", "symmetry_worst"]
