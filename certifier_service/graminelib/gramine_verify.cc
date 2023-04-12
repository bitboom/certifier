//  Copyright (c) 2022-23, VMware Inc, and the Certifier Authors.  All rights reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "gramineverify.h"

extern bool gramine_remote_verify_impl(const int what_to_say_size, byte* what_to_say, const int attestation_size, byte* attestation, int* measurement_out_size, byte* measurement_out);

bool gramine_Verify(const int what_to_say_size, byte* what_to_say,
    const int attestation_size, byte* attestation,
    int* measurement_out_size, byte* measurement_out) {
  bool result = false;

  result = gramine_remote_verify_impl
           (what_to_say_size, what_to_say, attestation_size,
            attestation, measurement_out_size, measurement_out);
  if (!result) {
    printf("Gramine verify failed\n");
    return false;
  }

  return true;

}
