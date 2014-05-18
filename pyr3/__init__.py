from cffi import FFI
ffi = FFI()

C = ffi.verify("""   // passed to the real C compiler
#include <r3/r3.h>
""", libraries=[], ext_package='pyr3')