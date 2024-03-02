v0.4.3
=====================================
## Minor features[¶](https://docs.djangoproject.com/en/5.0/releases/5.0/#minor-features)
1. [django.contrib.admin](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#module-django.contrib.admin)[¶](https://docs.djangoproject.com/en/5.0/releases/5.0/#django-contrib-admin)
The new [AdminSite.get_log_entries()](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.AdminSite.get_log_entries) method allows customizing the queryset for the site’s listed log entries.
The django.contrib.admin.AllValuesFieldListFilter, ChoicesFieldListFilter, RelatedFieldListFilter, and RelatedOnlyFieldListFilter admin filters now handle multi-valued query parameters.
XRegExp is upgraded from version 3.2.0 to 5.1.1.
The new [AdminSite.get_model_admin()](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.AdminSite.get_model_admin) method returns an admin class for the given model class.
Properties in [ModelAdmin.list_display](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display) now support boolean attribute.
jQuery is upgraded from version 3.6.4 to 3.7.1.
2. [django.contrib.auth](https://docs.djangoproject.com/en/5.0/topics/auth/#module-django.contrib.auth)[¶](https://docs.djangoproject.com/en/5.0/releases/5.0/#django-contrib-auth)
The default iteration count for the PBKDF2 password hasher is increased from 600,000 to 720,000.
The new asynchronous functions are now provided, using an a prefix: [django.contrib.auth.aauthenticate()](https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.aauthenticate), [aget_user()](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.aget_user), [alogin()](https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.alogin), [alogout()](https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.alogout), and [aupdate_session_auth_hash()](https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.aupdate_session_auth_hash).
AuthenticationMiddleware now adds an [HttpRequest.auser()](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.auser) asynchronous method that returns the currently logged-in user.
The new [django.contrib.auth.hashers.acheck_password()](https://docs.djangoproject.com/en/5.0/topics/auth/passwords/#django.contrib.auth.hashers.acheck_password) asynchronous function and [AbstractBaseUser.acheck_password()](https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#django.contrib.auth.models.AbstractBaseUser.acheck_password) method allow asynchronous checking of user passwords.
3. [django.contrib.contenttypes](https://docs.djangoproject.com/en/5.0/ref/contrib/contenttypes/#module-django.contrib.contenttypes)[¶](https://docs.djangoproject.com/en/5.0/releases/5.0/#django-contrib-contenttypes)
[QuerySet.prefetch_related()](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.prefetch_related) now supports prefetching [GenericForeignKey](https://docs.djangoproject.com/en/5.0/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericForeignKey) with non-homogeneous set of results.

**Full Changelog**: https://github.com/swastkk/automate_changelog/compare/v0.4.2...v0.4.3

v0.4.2
=====================================
What’s new in Django 5.0[¶](https://docs.djangoproject.com/en/5.0/releases/5.0/#what-s-new-in-django-5-0)
---------------

Facet filters in the admin[¶](https://docs.djangoproject.com/en/5.0/releases/5.0/#facet-filters-in-the-admin)
Facet counts are now shown for applied filters in the admin changelist when toggled on via the UI. This behavior can be changed via the new [ModelAdmin.show_facets](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.show_facets) attribute. For more information see [Facets](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/filters/#facet-filters).

**Full Changelog**: https://github.com/swastkk/automate_changelog/compare/v0.4.1...v0.4.2

CHANGELOG
==========

v0.4.1
=====================================
Added the Action Example
-----------------------------

The goal of this Action is to be the Action for committing files for the 80% use case. Therefore, you might run into issues if your Workflow falls into the not supported 20% portion.

The following is a list of edge cases the Action knowingly does not support:

No git pull when the repository is out of date with remote. The Action will not do a git pull before doing the git push. You are responsible for keeping the repository up to date in your Workflow runs.

No support for running the Action in build matrices. If your Workflow is using build matrices, and you want that each job commits and pushes files to the remote, you will run into the issue, that the repository in the workflow will become out of date. As the Action will not do a git pull for you, you have to do that yourself.

No support for git rebase or git merge. There are many strategies on how to integrate remote upstream changes to a local repository. git-auto-commit does not want to be responsible for doing that.

No support for detecting line break changes between CR (Carriage Return) and LF (Line Feed). This is a low level issue, you have to resolve differently in your project. Sorry.

If this Action doesn't work for your workflow, check out [EndBug/add-and-commit](https://github.com/EndBug/add-and-commit).

**Full Changelog**: https://github.com/swastkk/automate_changelog/compare/v0.4.0...v0.4.1


v0.4.0
=====================================
Tagging suggestions
-----------
It’s common practice to prefix your version names with the letter v. Some good tag names might be v1.0.0 or v2.3.4.

If the tag isn’t meant for production use, add a pre-release version after the version name. Some good pre-release versions might be v0.2.0-alpha or v5.9-beta.3.

Semantic versioning
-------
If you’re new to releasing software, we highly recommend to [learn more about semantic versioning.](http://semver.org/)

A newly published release will automatically be labeled as the latest release for this repository.

If 'Set as the latest release' is unchecked, the latest release will be determined by higher semantic version and creation date. [Learn more about release settings.](https://docs.github.com/repositories/releasing-projects-on-github/managing-releases-in-a-repository)

**Full Changelog**: https://github.com/swastkk/automate_changelog/compare/v0.3.9...v0.4.0

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

