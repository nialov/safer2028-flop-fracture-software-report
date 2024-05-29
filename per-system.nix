({ inputs, ... }:

  {
    perSystem = { self', config, system, pkgs, lib, ... }:
      let
        mkNixpkgs = nixpkgs:
          import nixpkgs {
            inherit system;
            overlays = let
              pandocXnosOverlay = _: prev: {

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
                        # postPatch = ''
                        #   substituteInPlace pandocxnos/core.py \
                        #       --replace-fail "'Cannot understand pandocversion=%s'%pandocversion" \
                        #       "f'{pandocversion} & {pattern}'"
                        # '';

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
                fd parallel toml2json miniserve watchexec pandoc pandoc-fignos
                pandoc-eqnos pandoc-secnos pandoc-tablenos gdal;
              inherit (pkgs.texlive.combined) scheme-medium;
              python3WithPackages = pkgs.python3.withPackages (p:
                lib.attrValues {
                  inherit (p)
                    typer jsonschema tomli ipython jinja2 j2cli jupyterlab
                    pandas openpyxl tabulate;
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
            runtimeInputs = self'.devShells.default.nativeBuildInputs;
            text = ''
              fd --extension toml . ./task_5_report | parallel "python3 ./task_5_report/validate_schema.py {}"
            '';
          };
          build = pkgs.writeShellApplication {
            name = "build";
            runtimeInputs = self'.devShells.default.nativeBuildInputs;
            text = ''
              python3 scripts/create_report.py
            '';
          };
          inherit (pkgs.python3Packages) pandoc-xnos;
        };

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
            yamllint = { enable = true; };
            commitizen.enable = true;
            ruff = { enable = true; };
          };

        };
      };

  })
