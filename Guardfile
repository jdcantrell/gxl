# A sample Guardfile
# More info at https://github.com/guard/guard#readme

# Add files and commands to this file, like the example:
#   watch(%r{file/path}) { `command(s)` }
#
guard 'shell' do
  watch(%r{^sass/(.*).sass}) {|m| system "compass compile" }
  watch(%r{^build/(.*).(js|css)}) {|m| system "hologram hologram.yml" }
  watch(%r{^assets/(.*).(js|css|html)}) {|m| system "hologram hologram.yml" }
end
