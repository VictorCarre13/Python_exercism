String twoFer([String? name]) {
  name = (name == null || name.isEmpty) ? "you" : name;
  return "One for $name, one for me.";
}