#!/bin/bash
# ##############################################################################
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
ISLET_INC="$HERE/include"
ISLET_LIB="$HERE/lib"

TARGET_HDR="$ISLET_SDK/include/islet.h"
TARGET_LIB="$ISLET/out/x86_64-unknown-linux-gnu/release/libislet_sdk.a"

# Sync islet
cd "$HERE"
rm -rf "$ISLET"
git clone https://github.com/islet-project/islet.git "$ISLET"
cd "$ISLET"
git submodule update --init --depth 1 $ISLET/assets
git submodule update --init --depth 1 $ISLET/third-party/ciborium
git submodule update --init --depth 1 $ISLET/third-party/coset

# Install rust to build ISLET SDK
"$ISLET/scripts/deps/rust.sh"

. "$HOME/.cargo/env"
# Build ISLET SDK (simulated version for x86_64)
cd "$ISLET_SDK" && make simulated

mkdir -p "$ISLET_INC" "$ISLET_LIB"
cp -p "$TARGET_HDR" "$ISLET_INC"
cp -p "$TARGET_LIB" "$ISLET_LIB"

echo "Restart your shell or source ~/.bashrc"
