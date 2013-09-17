/*
 * Copyright (C) 2011 Google Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License. You may obtain a copy of
 * the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations under
 * the License.
 */

package com.github.rosjava.rosjava_extras.hokuyo.scip20;

/**
 * @author damonkohler@google.com (Damon Kohler)
 */
public class TmException extends RuntimeException {

  public TmException(String status) {
    super(getMessage(status));
  }

  private static String getMessage(String status) {
    if (status.equals("01")) {
      return "Invalid control code.";
    }
    if (status.equals("04")) {
      return "Adjust mode is off when requested for time.";
    }

    return "Unknown status code: " + status;
  }
}
