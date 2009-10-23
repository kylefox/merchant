desc "Runs test suite."
task :test do
    sh "python tests/test_credit_card.py"
    puts
    sh "python tests/test_expiry_date.py"
end

desc "Run tests and generate an HTML coverage report (requires coverage.py)"
task :coverage do
    sh "rake test"
    sh "rm -rf tests/coverage"
    sh "coverage html --omit=test -d tests/coverage"
    if RUBY_PLATFORM.index('darwin') >= 0
      sh "open tests/coverage/index.html"
    end
end