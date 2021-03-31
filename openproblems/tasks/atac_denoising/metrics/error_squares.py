from ....tools.decorators import metric
from sklearn.metrics import mean_squared_error


@metric(metric_name="Mean error squares", maximize=False)
def mean_error_squares(adata):
    return mean_squared_error(
        adata.obsm["mode2_denoised"].data, adata.obsm["mode2"].data
    )
