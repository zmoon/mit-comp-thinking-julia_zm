# mit-comp-thinking-julia_zm
my hw solns for [mitmath/18S191](https://github.com/mitmath/18S191) (Fa20); playing with [Pluto](https://github.com/fonsp/Pluto.jl)/[Binder](https://mybinder.org/)

I am just trying to learn some Julia, so issues/PRs related to improving the code/understanding are welcome.

## Packages

### local

Add this repo's Project(`.toml`).
```
julia>]
pkg> add Pluto  # to main/default env
pkg> activate .
pkg> instantiate  # install the packages (if needed)
pkg> precompile  # why not
```

Or in one line without using Julia REPL:
```
julia -e 'import Pkg; Pkg.add(\"Pluto\"); Pkg.activate(\".\"); Pkg.instantiate(); Pkg.precompile()'
```

### background

The original versions of the Pluto notebooks include blocks for creating a temporary environment
```julia
begin
    using Pkg
    Pkg.activate(mktempdir())
end
```
and add needed packages to that environment.
```julia
begin
    Pkg.add(["PackageA", "PackageB", ...])
    using PackageA
    using PackageB
    ...
end
```

Packages already installed [are not duplicated](https://julialang.github.io/Pkg.jl/v1/environments/#**4.**-Working-with-Environments-1) when an environment wants the same version, but this can still end up taking a while if there is a new version of a package. And even the registry checking/updating part alone can take ~ 1 min.

This reason this is currently needed in Pluto notebooks is because even if you create a non-temporary environment and start Pluto from there, it won't necessarily be aware of the environment and the packages you have added to it.

> A Pluto notebook worker will probably run in a different package environment than the one you launched Pluto from. This is confusing - and will be changed at some point.

-- https://github.com/fonsp/Pluto.jl/blob/master/CONTRIBUTING.md

I can confirm that I did run in to this issue after changing such blocks to just imports...


### Binder

...
