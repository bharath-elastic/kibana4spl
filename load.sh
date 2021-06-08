  python load_template.py settings/weblogs_template.json weblogs
  python load_template.py settings/metricbeat_k4spl_template.json metricbeat-k4spl
  python ndjsonindexer.py data/weblogs.json weblogs
  python ndjsonindexer.py data/metricbeat-k4spl.json metricbeat-k4spl
