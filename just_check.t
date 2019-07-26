use Test::Text;

for my $dir (qw(. pois) ) {
  my $tesxt = Test::Text->new($dir, ".", "Spanish", @_);
  $tesxt->check();
}

done_testing;
