
Binder setup based on [fonsp/pluto-on-binder](https://github.com/fonsp/pluto-on-binder)
(maybe should have forked it),
which uses [jupyter-server-proxy](https://github.com/jupyterhub/jupyter-server-proxy).

Differences:
* not including `Manifest.toml`
  - note that when Binder sees `Project.toml`, it uses `JuliaProjectTomlBuildPack`

Notes:
* including `Project.toml` seems to activate the standard Jupyter Julia support (IJulia),
  which we don't need for Pluto
  - looks for `Manifest`/`Project.toml` in `REPO_DIR`
    - activates this project (environment), `instantiate`s (download dependencies),
      `resolve`s (update manifest), `precompile`s (all project dependencies)
    - if we don't include one in `binder/`, don't get `julia`,
      but the ones in `binder/` don't get installed to the default env
    - puts empty ones in repo root with current setup (`binder/`)
