#!/bin/bash
# Sends a request to that URL & displays the size of the body of the response
curl -sL "$1" | wc -c
