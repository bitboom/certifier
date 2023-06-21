#!/bin/bash

#  Copyright (c) 2023 Samsung Electronics Co., Ltd All Rights Reserved
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License

# ##############################################################################
# setup.sh - Setup script to build ISLET SDK
# ##############################################################################

set -Eeuo pipefail

CC_ROOT=$(git rev-parse --show-toplevel)
HERE="$CC_ROOT/third_party/islet"

ISLET="$HERE/remote"
ISLET_SDK="$ISLET/sdk"
ISLET_CLI="$ISLET/cli"
ISLET_INC="$HERE/include"
ISLET_LIB="$HERE/lib"
ISLET_TAG="certifier-v1.0.2-beta"
ISLET_TOOL="$HERE/tool"

TARGET_HDR="$ISLET_SDK/include/islet.h"
TARGET_LIB="$ISLET/out/x86_64-unknown-linux-gnu/debug/libislet_sdk.so"
TARGET_CLI="$ISLET_CLI/target/x86_64-unknown-linux-gnu/release/islet_cli"

# Sync Islet
cd "$HERE"
rm -rf "$ISLET_TAG.tar.gz"
wget https://github.com/Samsung/islet/archive/refs/tags/$ISLET_TAG.tar.gz
tar xf "$ISLET_TAG.tar.gz"
rm -rf "$ISLET"
mv islet-$ISLET_TAG "$ISLET"

# Install rust to build Islet SDK
"$ISLET/scripts/deps/rust.sh"

. "$HOME/.cargo/env"
# Build Islet SDK (simulated version for x86_64)
cd "$ISLET_SDK" && cargo build

mkdir -p "$ISLET_INC" "$ISLET_LIB" "$ISLET_TOOL"
cp -p "$TARGET_HDR" "$ISLET_INC"
cp -p "$TARGET_LIB" "$ISLET_LIB"

# Build Islet CLI
cd "$ISLET_CLI" && cargo build -r --target=x86_64-unknown-linux-gnu
cp -p "$TARGET_CLI" "$ISLET_TOOL"

echo "Restart your shell or source ~/.bashrc"
