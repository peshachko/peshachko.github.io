const lightbox = GLightbox();
// It is not clear whether .reload() is needed as this script is imported as an ES
// module (after the HTML is fully loaded).
document$.subscribe(() => { lightbox.reload(); });
