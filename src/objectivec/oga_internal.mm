// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.

#import "oga_internal.h"

@implementation OGAInt32Span {
  const int32_t* _ptr;
  size_t _size;
}

- (nullable instancetype)initWithDataPointer:(const int32_t*)pointer size:(size_t)size {
  _ptr = pointer;
  _size = size;
  return [self init];
}

- (const int32_t*)pointer {
  return _ptr;
}

- (size_t)size {
  return _size;
}

- (int32_t)lastElementWithError:(NSError**)error {
  if (_size == 0) {
    NSDictionary *errorDictionary = @{NSLocalizedDescriptionKey : @"The size of this span is invalid"};
    *error = [[NSError alloc] initWithDomain:kOgaErrorDomain code:-1 userInfo:errorDictionary];
    return -1;
  }
  return *(_ptr + (_size - 1));
}

@end

@implementation OGAInt64Span {
  const int64_t* _ptr;
  size_t _size;
}

- (nullable instancetype)initWithDataPointer:(const int64_t*)pointer size:(size_t)size {
  _ptr = pointer;
  _size = size;
  return [self init];
}

- (const int64_t*)pointer {
  return _ptr;
}

- (size_t)size {
  return _size;
}

- (int64_t)lastElementWithError:(NSError**)error {
  if (_size == 0) {
    NSDictionary *errorDictionary = @{NSLocalizedDescriptionKey : @"The size of this span is invalid"};
    *error = [[NSError alloc] initWithDomain:kOgaErrorDomain code:-1 userInfo:errorDictionary];
    return -1;
  }
  return *(_ptr + (_size - 1));
}

@end
