#!/bin/sh

echo "Waiting for MongoDB to start..."
./wait-for db:27017 