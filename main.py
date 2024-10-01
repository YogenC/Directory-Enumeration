import requests
import re

def sanitize_url(target_url):
    sanitized = re.sub(r'https?://', '', target_url)
    sanitized = re.sub(r'[^\w.-]', '_', sanitized)
    return sanitized


def brute_force_paths(target_url, wordlist=None, save_file=None):
    if wordlist is None:
        wordlist = [
            'admin', 'login', 'config', 'backup', 'user', 'test', 'dev', 'uploads',
            'debug', 'api', 'auth', 'private', 'server', 'php', 'database', 'files',
            'passwords', 'access', 'account', 'accounts', 'actions', 'admin_area',
            'administrator', 'ajax', 'analytics', 'app', 'apps', 'archive', 'archives',
            'assets', 'auth', 'authentication', 'authorize', 'backup_old', 'backups',
            'bin', 'browserconfig', 'bug', 'cache', 'captcha', 'cert', 'certificates',
            'cgi-bin', 'checkout', 'client', 'clients', 'common', 'components', 
            'config_backup', 'configuration', 'connect', 'console', 'contact', 'control', 
            'controlpanel', 'core', 'cpanel', 'css', 'custom', 'data', 'db', 'db_backup',
            'default', 'demo', 'deploy', 'deployment', 'development', 'diagnostics',
            'dir', 'direct', 'directory', 'docs', 'download', 'downloads', 'dump', 
            'dynamic', 'editor', 'email', 'emails', 'error', 'errors', 'event', 
            'example', 'examples', 'export', 'extensions', 'external', 'extras', 
            'favicon', 'feature', 'features', 'file', 'files_old', 'fileserver', 
            'filter', 'firewall', 'forgot', 'forgot_password', 'form', 'forms', 
            'framework', 'frontend', 'ftp', 'gateway', 'git', 'go', 'graphics', 'gui', 
            'help', 'hidden', 'history', 'home', 'hooks', 'htdocs', 'html', 'http',
            'https', 'icons', 'img', 'import', 'include', 'includes', 'index', 'info',
            'install', 'installation', 'integrations', 'internal', 'js', 'json', 
            'keys', 'lang', 'language', 'layout', 'lib', 'license', 'licenses', 
            'logs', 'logout', 'maintenance', 'manual', 'media', 'members', 'meta',
            'migration', 'mobile', 'modules', 'monitor', 'monitoring', 'mysql', 'name',
            'network', 'news', 'node', 'notifications', 'oauth', 'object', 'objects',
            'offline', 'old', 'operations', 'order', 'orders', 'org', 'out', 'output',
            'package', 'packages', 'panel', 'password', 'payment', 'payments', 'pdf', 
            'pending', 'permissions', 'phpinfo', 'phpmyadmin', 'plugin', 'plugins',
            'policy', 'portal', 'post', 'posts', 'preferences', 'preview', 'private', 
            'prod', 'production', 'profile', 'project', 'projects', 'properties', 
            'proxy', 'public', 'purchase', 'queries', 'query', 'queue', 'readme', 
            'recover', 'recovery', 'redirect', 'register', 'registration', 'repo', 
            'reports', 'request', 'requests', 'reset', 'resources', 'restricted', 
            'return', 'review', 'reviews', 'robots', 'root', 'rss', 'runtime', 
            'sales', 'sandbox', 'save', 'schema', 'scripts', 'search', 'secure', 
            'security', 'send', 'server', 'service', 'session', 'settings', 'share', 
            'shell', 'shop', 'site', 'sites', 'sitemap', 'smtp', 'software', 'source',
            'sources', 'sql', 'ssl', 'staff', 'stage', 'staging', 'static', 'status', 
            'storage', 'store', 'style', 'styles', 'submissions', 'subscribe', 'support',
            'sync', 'sysadmin', 'system', 'task', 'tasks', 'team', 'templates', 'test',
            'testing', 'theme', 'themes', 'tmp', 'token', 'tools', 'transactions', 
            'translate', 'translation', 'trust', 'tutorial', 'tutorials', 'upgrade',
            'uploads', 'user', 'users', 'util', 'utils', 'validation', 'vendor', 'verify', 
            'version', 'versions', 'video', 'videos', 'view', 'views', 'virtual', 
            'vulnerability', 'vulnerabilities', 'web', 'webadmin', 'webapps', 
            'webconfig', 'webmaster', 'website', 'widgets', 'windows', 'wordpress', 
            'wp-admin', 'wp-content', 'wp-includes', 'xml', 'xss', 'zip', 'zipped'
        ]

    
    if save_file is None:
        save_file = sanitize_url(target_url) + '.txt'

    found_paths = []

    for word in wordlist:
        url = f"{target_url.rstrip('/')}/{word}"
        
        try:
            response = requests.get(url)

            if response.status_code == 200:
                print(f"Found 200 at: {url}")
                found_paths.append(url)
            else:
                print(f"{url} (Status Code: {response.status_code})")
        
        except requests.exceptions.RequestException as e:
            print(f"Error accessing {target_url}, domain is probably wrong...")
            return

    if found_paths:
        with open(save_file, 'w') as f:
            for path in found_paths:
                f.write(f"{path}\n")
        print(f"Saved found paths to {save_file}")
    else:
        print("No valid paths found.")

    return found_paths

if __name__ == "__main__":
    target = input("Enter the target URL with port if needed (e.g., http://example.com): ")
    
    if not target.startswith('http://') and not target.startswith('https://'):
        target = 'http://' + target

    custom_wordlist = input("Do you want to use a custom wordlist? Enter the file path or press Enter to use the default: ")

    wordlist = None
    if custom_wordlist:
        with open(custom_wordlist, 'r') as f:
            wordlist = [line.strip() for line in f.readlines()]

    brute_force_paths(target, wordlist)
