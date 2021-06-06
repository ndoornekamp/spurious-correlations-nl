const languageSetters = document.querySelectorAll('.set-language')

languageSetters.forEach(languageSetter =>
    languageSetter.addEventListener('click', function(){setlanguage(languageSetter.dataset.language)})
)

async function setlanguage(language) {
    const response = await fetch('/set_language', {method: 'POST', body: JSON.stringify({'language': language})})
    const data = await response.json()

    if (data['changed_language']) {
        console.log(`Changed language to ${language}`)
        location.reload()
    }
}
