FILEFORGE Product Requirements Document
Original problem statement
Build FILEFORGE, a standalone premium futuristic dark file-processing workspace named “Your Files. Your Tools. One Powerful Workspace.” It must present all 33 PDF, image/video, converter, and utility tools as independent screens with local-first processing, responsive navigation, persistent local history, search, settings, privacy messaging, and no fake success states. The first delivery choice was: build all 33 screens now, with each tool’s core function working and advanced processing added progressively.

Personas
Everyday users who need a quick, private file conversion or calculation without creating an account.
Creators and office workers moving between PDF, image, document, and data formats.
Privacy-conscious users who want browser-local processing and transparent limitations.
Architecture decisions
React 19 with the existing CRA/Craco starter and React Router routes.
One reusable tool directory model drives cards, categories, search, related tools, and all 33 /tool/:slug screens.
LocalStorage stores non-sensitive processing metadata only; passwords and file contents are never stored.
Browser APIs provide file selection, downloads, crypto-safe password generation, canvas image processing, and utility calculations.
No backend API is required for the local-first MVP; the existing protected environment configuration remains untouched.
Futuristic neon visual system follows /app/design_guidelines.json, with responsive CSS and role-based data-testid attributes.
Core requirements
 FILEFORGE branding, hero workspace, privacy-first message, stats, popular tools, and category navigation.
 All 33 tools listed across PDF Tools, Image & Video, and Converters & Utilities.
 Independent route and processing workspace for every tool.
 Global tool search, directory search, category filtering, related tools, and responsive navigation.
 Local image canvas processing for core image conversion/compression/resize flows.
 Working word counter, JSON formatting/validation, Base64, secure password, percentage, EMI, BMI, and age utilities.
 Local history metadata with clear action and no sensitive content.
 Settings controls, responsive mobile menu, browser-local privacy disclosure, and real download actions.
Implementation log
2026-11-06
Replaced the starter splash with the FILEFORGE workspace UI.
Added the 33-tool data model, directory, category pages, dynamic tool screens, global search, history, and settings routes.
Added responsive neon-dark visual system, upload zones, processing states, utility panels, and localStorage history.
Fixed mobile All Tools routing and removed premature home-upload history writes.
Replaced generic fake file results with real canvas outputs for supported image flows and honest limitation messaging for advanced formats still in progress.
Production build and frontend browser flows verified.
Prioritized backlog
P0 — next core product work
Add pdf-lib and PDF.js for actual merge, split, rotate, JPG/PDF, and supported protection workflows.
Add Mammoth/DOCX generation for PDF-to-Word and Word-to-PDF flows with clear OCR limitations.
Add FFmpeg.wasm for real local video-to-MP3 processing with progress reporting.
P1 — broaden format coverage
Add HEIC decoding, XLSX reading, QR generation, barcode generation, and text-to-PDF export libraries.
Add IndexedDB file metadata and generated-result references for the Files section.
Add per-tool options such as quality sliders, page ranges, resize dimensions, and crop controls.
P2 — polish and power features
Lazy-load heavy processors and move large operations into Web Workers.
Add tool-specific previews, richer error diagnostics, and accessible keyboard shortcuts.
Add import/export for non-sensitive history metadata and a focused privacy/about view.