#!/usr/bin/env python

import argparse

from data_generator import DataWriter
from config_parser import parse_default_config

def generate_data(**kvargs):
    config = parse_default_config(kvargs['config_fn'])
    data_path = config.get("data_path")
    data_size = config.get("data_size")
    scale = config.get("scale")
    index_col_name = config.get("index_col_name")
    value_col_name = config.get("value_col_name")
    data_writer = DataWriter(data_size, scale, index_col_name, value_col_name)
    data_writer.generate_and_write(data_path)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_fn", default="", type=str)
    return parser.parse_args()
    
def main():
    args = parse_arguments()
    generate_data(**vars(args))
    
if __name__ == '__main__':
    main()

