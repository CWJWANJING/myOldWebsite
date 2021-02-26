# CWJWANJING.github.io

## Development instructions

To see the changes you made while developing, run the following command from the root directory of the project:

```
$ make devserver
```

This will make your site accessible (locally) at [http://localhost:8000](http://localhost:8000).

Once you are happy with your changes, run the following:

```
# commit and push to the master branch
# -p will ask you to confirm each change you've made
git add -p .
git commit
git push

# push to the gh-pages branch (make changes visible)
make github
```
