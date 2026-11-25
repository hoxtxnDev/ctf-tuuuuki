require_relative 'libronsolve'

EXE = File.join(__dir__, '..', 'challenge', 'src', 'bug-me')
if `#{ EXE } \"#{ expected_flag() }\"` =~ /YAY/
  if `#{ EXE } \"dUOC{residuos_teorema_chino_62841}\"` =~ /YAY/
    raise 'Uh oh, a bad flag worked!'
  end

  puts 'Looks good!'
  exit(0)
end

raise "Uh oh, the correct flag didn't work!"
