const localeSetters = document.querySelectorAll('.set-locale')

localeSetters.forEach(localeSetter =>
    localeSetter.addEventListener('click', function(){setLocale(localeSetter.dataset.locale)})
)

async function setLocale(locale) {
    const response = await fetch('/set_locale', {method: 'POST', body: JSON.stringify({'locale': locale})})
    const data = await response.json()

    if (data['changed_locale']) {
        console.log(`Changed locale to ${locale}`)
        location.reload()
    }
}
