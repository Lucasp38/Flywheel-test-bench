"""
Si c'est utilisé à plusieurs endroits ET que c'est générique  et indépendant
utils/
├── __init__.py
├── helpers.py          ← Fonctions générales
├── file_utils.py       ← Gestion fichiers
├── math_utils.py       ← Calculs génériques
├── validation.py       ← Validations
├── logger.py           ← Configuration logs
├── config.py           ← Gestion configuration
└── constants.py        ← Constantes globales
"""

import logging as log



log.basicConfig(filename="test.log",format='%(levelname)s:%(message)s', level=log.DEBUG)
log.debug('This message should appear on the console')
log.info('So should this')
log.warning('And this, too')


"""
class FileLogger:
    def __init__(self, filename):
        self.filename = filename
"""