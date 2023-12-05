{"payload":{"allShortcutsEnabled":false,"fileTree":{"0x03-python-data_structures":{"items":[{"name":"0-print_list_integer.py","path":"0x03-python-data_structures/0-print_list_integer.py","contentType":"file"},{"name":"1-element_at.py","path":"0x03-python-data_structures/1-element_at.py","contentType":"file"},{"name":"10-divisible_by_2.py","path":"0x03-python-data_structures/10-divisible_by_2.py","contentType":"file"},{"name":"100-print_python_list_info.c","path":"0x03-python-data_structures/100-print_python_list_info.c","contentType":"file"},{"name":"11-delete_at.py","path":"0x03-python-data_structures/11-delete_at.py","contentType":"file"},{"name":"12-switch.py","path":"0x03-python-data_structures/12-switch.py","contentType":"file"},{"name":"13-is_palindrome.c","path":"0x03-python-data_structures/13-is_palindrome.c","contentType":"file"},{"name":"2-replace_in_list.py","path":"0x03-python-data_structures/2-replace_in_list.py","contentType":"file"},{"name":"3-print_reversed_list_integer.py","path":"0x03-python-data_structures/3-print_reversed_list_integer.py","contentType":"file"},{"name":"4-new_in_list.py","path":"0x03-python-data_structures/4-new_in_list.py","contentType":"file"},{"name":"5-no_c.py","path":"0x03-python-data_structures/5-no_c.py","contentType":"file"},{"name":"6-print_matrix_integer.py","path":"0x03-python-data_structures/6-print_matrix_integer.py","contentType":"file"},{"name":"7-add_tuple.py","path":"0x03-python-data_structures/7-add_tuple.py","contentType":"file"},{"name":"8-multiple_returns.py","path":"0x03-python-data_structures/8-multiple_returns.py","contentType":"file"},{"name":"9-max_integer.py","path":"0x03-python-data_structures/9-max_integer.py","contentType":"file"},{"name":"README.md","path":"0x03-python-data_structures/README.md","contentType":"file"},{"name":"lists.h","path":"0x03-python-data_structures/lists.h","contentType":"file"}],"totalCount":17},"":{"items":[{"name":"0x00-python-hello_world","path":"0x00-python-hello_world","contentType":"directory"},{"name":"0x01-python-if_else_loops_functions","path":"0x01-python-if_else_loops_functions","contentType":"directory"},{"name":"0x02-python-import_modules","path":"0x02-python-import_modules","contentType":"directory"},{"name":"0x03-python-data_structures","path":"0x03-python-data_structures","contentType":"directory"},{"name":"0x04-python-more_data_structures","path":"0x04-python-more_data_structures","contentType":"directory"},{"name":"0x05-python-exceptions","path":"0x05-python-exceptions","contentType":"directory"},{"name":"0x06-python-classes","path":"0x06-python-classes","contentType":"directory"},{"name":"0x07-python-test_driven_development","path":"0x07-python-test_driven_development","contentType":"directory"},{"name":"0x08-python-more_classes","path":"0x08-python-more_classes","contentType":"directory"},{"name":"0x09-python-everything_is_object","path":"0x09-python-everything_is_object","contentType":"directory"},{"name":"0x0A-python-inheritance","path":"0x0A-python-inheritance","contentType":"directory"},{"name":"0x0B-python-input_output","path":"0x0B-python-input_output","contentType":"directory"},{"name":"0x0C-python-almost_a_circle","path":"0x0C-python-almost_a_circle","contentType":"directory"},{"name":"0x0D-SQL_introduction","path":"0x0D-SQL_introduction","contentType":"directory"},{"name":"0x0E-SQL_more_queries","path":"0x0E-SQL_more_queries","contentType":"directory"},{"name":"0x0F-python-object_relational_mapping","path":"0x0F-python-object_relational_mapping","contentType":"directory"},{"name":"0x10-python-network_0","path":"0x10-python-network_0","contentType":"directory"},{"name":"0x11-python-network_1","path":"0x11-python-network_1","contentType":"directory"},{"name":"0x12-javascript-warm_up","path":"0x12-javascript-warm_up","contentType":"directory"},{"name":"0x13-javascript_objects_scopes_closures","path":"0x13-javascript_objects_scopes_closures","contentType":"directory"},{"name":"0x14-javascript-web_scraping","path":"0x14-javascript-web_scraping","contentType":"directory"},{"name":"0x15-javascript-web_jquery","path":"0x15-javascript-web_jquery","contentType":"directory"},{"name":"README.md","path":"README.md","contentType":"file"}],"totalCount":23}},"fileTreeProcessingTime":7.487858,"foldersToFetch":[],"reducedMotionEnabled":null,"repo":{"id":649787392,"defaultBranch":"main","name":"alx-higher_level_programming","ownerLogin":"CipherPhantom","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2023-06-05T16:25:16.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/104349927?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"main","listCacheKey":"v0:1685982317.565203","canEdit":false,"refType":"branch","currentOid":"34671ff6d381b5b9f9bc8f61a4c599fe7586cc5e"},"path":"0x03-python-data_structures/2-replace_in_list.py","currentUser":null,"blob":{"rawLines":["#!/usr/bin/python3","def replace_in_list(my_list, idx, element):","    if idx < 0 or idx > len(my_list) - 1:","        return my_list","    for i in range(len(my_list)):","        if idx == i:","            my_list[i] = element","            return my_list"],"stylingDirectives":[[{"start":0,"end":18,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":19,"cssClass":"pl-en"},{"start":20,"end":27,"cssClass":"pl-s1"},{"start":29,"end":32,"cssClass":"pl-s1"},{"start":34,"end":41,"cssClass":"pl-s1"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":15,"end":17,"cssClass":"pl-c1"},{"start":18,"end":21,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":27,"cssClass":"pl-en"},{"start":28,"end":35,"cssClass":"pl-s1"},{"start":37,"end":38,"cssClass":"pl-c1"},{"start":39,"end":40,"cssClass":"pl-c1"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":22,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":9,"cssClass":"pl-s1"},{"start":10,"end":12,"cssClass":"pl-c1"},{"start":13,"end":18,"cssClass":"pl-en"},{"start":19,"end":22,"cssClass":"pl-en"},{"start":23,"end":30,"cssClass":"pl-s1"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":14,"cssClass":"pl-s1"},{"start":15,"end":17,"cssClass":"pl-c1"},{"start":18,"end":19,"cssClass":"pl-s1"}],[{"start":12,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-s1"},{"start":23,"end":24,"cssClass":"pl-c1"},{"start":25,"end":32,"cssClass":"pl-s1"}],[{"start":12,"end":18,"cssClass":"pl-k"},{"start":19,"end":26,"cssClass":"pl-s1"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/CipherPhantom/alx-higher_level_programming/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null,"repoAlertsPath":"/CipherPhantom/alx-higher_level_programming/security/dependabot","repoSecurityAndAnalysisPath":"/CipherPhantom/alx-higher_level_programming/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"2-replace_in_list.py","displayUrl":"https://github.com/CipherPhantom/alx-higher_level_programming/blob/main/0x03-python-data_structures/2-replace_in_list.py?raw=true","headerInfo":{"blobSize":"243 Bytes","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"3f26a72","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FCipherPhantom%2Falx-higher_level_programming%2Fblob%2Fmain%2F0x03-python-data_structures%2F2-replace_in_list.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"8","truncatedSloc":"8"},"mode":"executable file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":false,"newDiscussionPath":"/CipherPhantom/alx-higher_level_programming/discussions/new","newIssuePath":"/CipherPhantom/alx-higher_level_programming/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/CipherPhantom/alx-higher_level_programming/blob/main/0x03-python-data_structures/2-replace_in_list.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/CipherPhantom/alx-higher_level_programming/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"rawBlobUrl":"https://github.com/CipherPhantom/alx-higher_level_programming/raw/main/0x03-python-data_structures/2-replace_in_list.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"CipherPhantom","repoName":"alx-higher_level_programming","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timedOut":false,"notAnalyzed":false,"symbols":[{"name":"replace_in_list","kind":"function","identStart":23,"identEnd":38,"extentStart":19,"extentEnd":242,"fullyQualifiedName":"replace_in_list","identUtf16":{"start":{"lineNumber":1,"utf16Col":4},"end":{"lineNumber":1,"utf16Col":19}},"extentUtf16":{"start":{"lineNumber":1,"utf16Col":0},"end":{"lineNumber":7,"utf16Col":26}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/CipherPhantom/alx-higher_level_programming/branches":{"post":"UBwveWM0yAlfyOM0jMfqIZzPAfELhyJzXCUBJC5p29n9DNOWGG3szAKsMRL8xgn5Dyp7zCLvBUdKIc6aHBWPBA"},"/repos/preferences":{"post":"z0wu0OgQZOoFXQI_LZfPNYfX9FJEb-gYwwXk4wT7obdn1nM5BVkZxfjk4yOaoTTObFrv8XHXRpsksCeP4MAg3Q"}}},"title":"alx-higher_level_programming/0x03-python-data_structures/2-replace_in_list.py at main · CipherPhantom/alx-higher_level_programming"}