#!/bin/bash

protoc -I. --python_out=./ ./protos/interaction.proto

