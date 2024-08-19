from model.product_comparsion import ProdructComparison
import sys

if __name__ == '__main__':
    yaml_path = sys.argv[1]
    comp_obj = ProdructComparison(yaml_path)
    comp_obj.compare()
