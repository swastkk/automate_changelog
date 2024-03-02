v0.3.9
=====================================
Deploy to develop pipeline https://github.com/nexB/scancode.io/issues/659 by @tdruez in https://github.com/nexB/scancode.io/pull/666
Add attribution generation as a new downloadable output https://github.com/nexB/scancode.io/issues/684 by @tdruez in https://github.com/nexB/scancode.io/pull/712
Add pathmap pipes module for path matching using Aho-Corasick https://github.com/nexB/scancode.io/issues/711 by @tdruez in https://github.com/nexB/scancode.io/pull/713
Improve performances of map_jar_to_source pipe https://github.com/nexB/scancode.io/issues/711 by @tdruez in https://github.com/nexB/scancode.io/pull/723
File viewer search and full screen by @tdruez in https://github.com/nexB/scancode.io/pull/725

**Full Changelog**: https://github.com/swastkk/automate_changelog/compare/v0.3.7...v0.3.9

v0.3.0
=====================================
- Rename multiple pipelines for consistency and precision:
  - docker: analyze_docker_image
  - root_filesystems: analyze_root_filesystem_or_vm_image
  - docker_windows: analyze_windows_docker_image
  - inspect_manifest: inspect_packages
  - deploy_to_develop: map_deploy_to_develop
  - scan_package: scan_single_package

A data migration is included to facilitate the migration of existing data. Only the new names are available in the web UI but the REST API and CLI are backward compatible with the old names. [Issue #1044](https://github.com/nexB/scancode.io/issues/1044)

- Generate CycloneDX SBOM in 1.5 spec format, migrated from 1.4 previously. The Package vulnerabilities are now included in the CycloneDX SBOM when available. [Issue #807](https://github.com/nexB/scancode.io/issues/807)
- Improve the inspect_manifest pipeline to accept archives as inputs. [Issue #1034](https://github.com/nexB/scancode.io/issues/1034)
- Add support for tagging download URL inputs using the # section of URLs. 
  This feature is particularly useful in the map_develop_to_deploy pipeline when download URLs are utilized as inputs. Tags such as from and to can be specified by adding #from or #to fragments at the end of the download URLs. Using the CLI, the uploaded files can be tagged using the filename:tag syntax while using the --input-file arguments. In the UI, tags can be edited from the Project details view Inputs panel. On the REST API, a new upload_file_tag field is available to use along the upload_file. [Issue #708](https://github.com/nexB/scancode.io/issues/708)

**Full Changelog**: https://github.com/swastkk/automate_changelog/compare/v0.2.6...v0.3.0

