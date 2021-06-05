Dutch version of https://www.tylervigen.com/spurious-correlations

### Updating translations
1. Extract new strings to be translated using `pybabel extract -F babel.cfg -k _l -o messages.pot .`
2. Provide new translations in the `messages.pot` file
3. Compile using `pybabel update -i messages.pot -d app/translations`

For a full guide, see. e.g. https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n
