({ inputs, ... }:

  {
    perSystem = { self', config, system, pkgs, lib, ... }:
      let
        mkNixpkgs = nixpkgs:
          import nixpkgs {
            inherit system;
            overlays = let
              nixpkgsPandoc = import inputs.nixpkgs-pandoc { inherit system; };
              pandocXnosOverlay = final: prev: {
                inherit (nixpkgsPandoc) pandoc;

                pandoc-xnos-merged = prev.symlinkJoin {
                  name = "pandoc-xnos-merged";
                  paths = lib.attrValues {
                    inherit (final)
                      pandoc-fignos pandoc-eqnos pandoc-secnos pandoc-tablenos;
                    inherit (final.python3Packages) pandoc-xnos;
                  };
                };
                pythonPackagesExtensions = prev.pythonPackagesExtensions ++ [
                  (_: pythonPrev: {

                    pandoc-xnos = pythonPrev.pandoc-xnos.overridePythonAttrs
                      (_: {

                        patches = [
                          (prev.fetchpatch {
                            name =
                              "extended-regex-to-work-with-pandoc-version-3.patch";
                            url =
                              "https://patch-diff.githubusercontent.com/raw/tomduck/pandoc-xnos/pull/29.patch";
                            hash =
                              "sha256-j6xaFXo3jtXGPL58aIp8RTqeQZhJ8cVKL/iUbUhXBF0=";
                          })
                        ];

                      });
                  })
                ];

              };

            in [
              inputs.nix-extra.overlays.default
              pandocXnosOverlay

            ];
            config = { allowUnfree = true; };
          };

      in {
        _module.args.pkgs = mkNixpkgs inputs.nixpkgs;
        devShells = {
          default = pkgs.mkShell {
            buildInputs = lib.attrValues {

              inherit (pkgs)
                fd parallel toml2json miniserve watchexec pandoc
                pandoc-xnos-merged gdal;
              inherit (pkgs.texlive.combined) scheme-medium;
              python3WithPackages = pkgs.python3.withPackages (p:
                lib.attrValues {
                  inherit (p)
                    typer jsonschema tomli ipython jinja2 j2cli jupyterlab
                    pandas openpyxl tabulate bibtexparser;
                });

            };
            shellHook = config.pre-commit.installationScript + ''
              export PROJECT_DIR="$PWD"
            '';
          };

        };

        packages = {
          validate = pkgs.writeShellApplication {
            name = "validate";
            runtimeInputs = self'.devShells.default.buildInputs;
            text = ''
              fd --extension toml . ./src/software/ | parallel "python3 ./scripts/validate_schema.py {}"
            '';
          };
          build = pkgs.writeShellApplication {
            name = "build";
            runtimeInputs = self'.devShells.default.buildInputs;
            text = ''
              python3 scripts/create_report.py --html-template-path=${inputs.easy-pandoc-templates}/html/easy_template.html
            '';
          };
          inherit (pkgs.python3Packages) pandoc-xnos;
          inherit (pkgs) pandoc-xnos-merged;
        };

        checks = self'.packages;
        legacyPackages = pkgs;

        pre-commit = {
          check.enable = true;
          settings.hooks = {
            nixfmt.enable = true;
            black.enable = true;
            black-nb.enable = true;
            nbstripout.enable = true;
            isort = { enable = true; };
            shellcheck.enable = true;
            statix.enable = true;
            deadnix.enable = true;
            rstcheck.enable = true;
            yamllint = {
              enable = true;
              raw = { args = lib.mkBefore [ "-d" "relaxed" ]; };
            };
            commitizen.enable = true;
            ruff = { enable = true; };
          };

        };
      };

  })
