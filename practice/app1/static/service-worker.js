// self.addEventListener('install', (event) => {
//     event.waitUntil(
//         caches.open('form-cache').then((cache) => {
//             return cache.addAll(['/offline.html']);
//         })
//     );
// });

// self.addEventListener('fetch', (event) => {
//     event.respondWith(
//         fetch(event.request).catch(() => {
//             return caches.match(event.request).then((response) => {
//                 if (response) {
//                     return response;
//                 } else {
//                     return caches.match('/offline.html');
//                 }
//             });
//         })
//     );
// });

// self.addEventListener('sync', (event) => {
//     if (event.tag === 'sync-forms') {
//         event.waitUntil(syncForms());
//     }
// });

// async function syncForms() {
//     const db = await openDB('form-submissions', 1, {
//         upgrade(db) {
//             db.createObjectStore('forms', { keyPath: 'id', autoIncrement: true });
//         }
//     });
//     const forms = await db.getAll('forms');
//     for (const form of forms) {
//         await fetch('/submit_form/', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify(form)
//         });
//         await db.delete('forms', form.id);
//     }
// }
