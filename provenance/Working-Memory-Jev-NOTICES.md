# Third-party software

The proprietary [repository license](Working-Memory-Jev-LICENSE.txt) applies only to material owned or controlled by AustinAWay. It does not replace the terms of the libraries, model, tools, or hosted services used by this project. Their owners retain their rights.

This repository distributes application source and dependency manifests. Installed Python packages, `node_modules`, virtual environments, and compiled frontend output are not included in the source publication. Installing dependencies retrieves separately licensed material. A built browser bundle incorporates dependency code; anyone authorized to distribute a build must also preserve the notices and satisfy the licenses of the components included in it.

## Direct runtime and build components

The license identifiers below were checked against the installed package metadata used for this publication. The authoritative texts ship with the respective packages and projects.

| Component | Role | License | Project |
|---|---|---|---|
| FastAPI | Local HTTP API | MIT | [fastapi/fastapi](https://github.com/fastapi/fastapi) |
| Uvicorn | ASGI server | BSD-3-Clause | [encode/uvicorn](https://github.com/encode/uvicorn) |
| HTTPX | Server-side provider requests | BSD-3-Clause | [encode/httpx](https://github.com/encode/httpx) |
| spaCy | English source parsing | MIT | [explosion/spaCy](https://github.com/explosion/spaCy) |
| en_core_web_sm 3.8.0 | English parser model | MIT | [spaCy model release](https://github.com/explosion/spacy-models/releases/tag/en_core_web_sm-3.8.0) |
| python-dotenv | Private local configuration | BSD-3-Clause | [theskumar/python-dotenv](https://github.com/theskumar/python-dotenv) |
| React and React DOM | Browser interface | MIT | [facebook/react](https://github.com/facebook/react) |
| Lucide React | Interface icons | ISC | [lucide-icons/lucide](https://github.com/lucide-icons/lucide) |
| Vite | Browser development/build tooling | MIT | [vitejs/vite](https://github.com/vitejs/vite) |

This table is a guide to direct components, not a complete transitive license inventory. Exact Python packages are pinned in [requirements.lock](https://github.com/AustinAWay/Working-Memory-Jev/blob/main/requirements.lock); frontend packages are pinned in [web/package-lock.json](https://github.com/AustinAWay/Working-Memory-Jev/blob/main/web/package-lock.json). Those environments also contain transitive dependencies and test/build tools with their own terms. Review the installed distribution metadata and bundled notices before redistributing any packaged environment or compiled release.

## Hosted inference and research

Jev is accessed through TypeSafe's hosted API; Jev model weights are not distributed by this repository. API access, pricing, processing, and model rights are subject to the provider's terms. The repository owner's evaluation permission does not supply provider credentials or waive provider fees.

Research papers are linked and discussed in the documentation; their copyrights remain with their respective owners. Citing a paper does not mean its authors endorse or validate this application. Public-domain rights, statutory exceptions, and separately licensed material are not restricted by the repository's proprietary license.
