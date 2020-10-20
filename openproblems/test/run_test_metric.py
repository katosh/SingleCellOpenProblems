import sys
import openproblems
import anndata
import numbers
from openproblems.test import utils

utils.ignore_warnings()


def test_method(task, data_path, metric):
    adata = anndata.read_h5ad(data_path)
    m = metric(adata)
    assert isinstance(m, numbers.Number)


def main(task_name, metric_name, data_path):
    openproblems.data.no_cleanup()
    task = getattr(openproblems.tasks, task_name)
    metric = getattr(task.metrics, metric_name)
    test_method(task, data_path, metric)


if __name__ == "__main__":
    main(*sys.argv[1:])
