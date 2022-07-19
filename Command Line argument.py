import sys

print( f"sys.argv = { sys.argv } and type( sys.argv ) = { type( sys.argv ) }" )

"""
import argparse

parser = argparse.ArgumentParser()
print( f"1. parser = { parser } and type( parser ) = { type( parser ) }\n" )

parser.add_argument( '-o', "--Output", help = "Show Output" )
args = parser.parse_args()

print( f"2. parser = { parser } and type( parser ) = { type( parser ) }" )
print( f"2. args = { args } and type( args ) = { type( args ) }" )
print( f"2. args.Output = { args.Output } and type( args.Output ) = { type( args.Output ) }\n" )
"""
