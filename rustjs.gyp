{
  'targets': [
    {
      'target_name': 'rustjs_deps',
      'type': 'static_library',
      'dependencies': [
        'deps/v8/tools/gyp/v8.gyp:v8',
        'deps/v8/tools/gyp/v8.gyp:v8_libplatform'
      ],
      'include_dirs': [
        'deps/v8' # include/v8_platform.h
      ],
      'sources': [
        'deps/index.h',
        # node.gyp is added to the project by default.
        'common.gypi',
      ]
    }
  ]
}