const CACHE_NAME = 'accessable-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/web-accessibility-tools.html',
  '/static/styles.css',
  '/static/script.js',
  '/static/favicon.ico'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
