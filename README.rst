It is fork of Microsoft Translator API implementation by http://openlabs.co.in/.
https://github.com/openlabs/Microsoft-Translator-Python-API

Two new methods have been added/


GetTranslations Method. Retrieves an array of translations for a given language.
+++++++++++++++++++++++
::

        >>> from microsofttranslator import Translator
        >>> translator = Translator('<Your Client ID>', '<Your Client Secret>')
        >>> translator.get_translations('sun', 'ru', 'en')
        {'From': 'en', 'Translations': [{'TranslatedText': 'Солнце', 'MatchedOriginalText': '', 'Count': 0, 'MatchDegree': 100, 'Rating': 5}, {'TranslatedText': 'Солнце', 'MatchedOriginalText': 'sun', 'Count': 1, 'MatchDegree': 100, 'Rating': 1}, {'TranslatedText': 'солнце', 'MatchedOriginalText': 'sun', 'Count': 1, 'MatchDegree': 100, 'Rating': 1}, {'TranslatedText': 'ВС', 'MatchedOriginalText': 'SUN', 'Count': 1, 'MatchDegree': 99, 'Rating': 1}, {'TranslatedText': 'Вос', 'MatchedOriginalText': 'Sun', 'Count': 1, 'MatchDegree': 99, 'Rating': 1}, {'TranslatedText': 'Воскресенье', 'MatchedOriginalText': 'Sun', 'Count': 1, 'MatchDegree': 99, 'Rating': 1}, {'TranslatedText': 'Вс', 'MatchedOriginalText': 'Sun', 'Count': 1, 'MatchDegree': 99, 'Rating': 1}, {'TranslatedText': 'СОЛНЦЕ!!', 'MatchedOriginalText': 'SUN!!', 'Count': 0, 'MatchDegree': 63, 'Rating': 0}]}

Speak Method. Returns a string which is a URL to a wave or mp3 stream of the passed-in text being spoken in the desired language.
+++++++++++++++++++++++

::

        >>> from microsofttranslator import Translator
        >>> translator = Translator('<Your Client ID>', '<Your Client Secret>')
        >>> translator.speak('sun','en')
        'http://api.microsofttranslator.com/V2/http.svc/Speak?appId=<access_token>&text=sun&language=en&format=audio%2fwav&options=MinSize'


