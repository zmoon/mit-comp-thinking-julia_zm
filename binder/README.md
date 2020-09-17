
Binder setup based on [fonsp/pluto-on-binder](https://github.com/fonsp/pluto-on-binder)
(maybe should have forked it),
which uses [jupyter-server-proxy](https://github.com/jupyterhub/jupyter-server-proxy).

Differences:
* not including `Manifest.toml`
* precompiling after image is built (like [fonsp/PlutoUtils.jl/docker](https://github.com/fonsp/PlutoUtils.jl/tree/master/docker))

Notes:
* including `Project.toml` seems to activate the standard Jupyter Julia support (IJulia),
  which we don't need for Pluto
  - assumes Manifest/Project are in REPO_DIR
    - activates this, `instantiate`s (download dependencies), `resolve`s (update manifest), 
      `precompile`s (all project dependencies)
