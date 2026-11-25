<?php
if (isset($_GET['exif_shard']) || isset($_GET['page_token'])) {
    usleep(1800000);
    $s = intval($_GET['exif_shard'] ?? 1);
    $n = $s + 1;
    $tk = substr(hash('sha256', "exif_stream:$n"), 0, 14);
    header('Content-Type: application/json; charset=utf-8');
    $chunks = [];
    for ($i = 0; $i < 48; $i++) {
        $h = hash('sha512', "exif:$s:$i:$tk");
        $chunks[] = [
            "chunk_id" => ($s * 48) + $i,
            "vfs_path" => "pіcture.php?fіle=..%2f..%2fflаg.txt",
            "icc_profile_tag" => "छवि-मेटाडेटा-खंड-$s-$i-༄༅།།པར་རིས་གསང་བ་-$i-სურათის-ინდექსი",
            "raw_ifd_bytes" => substr($h, 0, 80)
        ];
    }
    echo json_encode([
        "status" => "partial_exif_ifd_dump",
        "shard" => $s,
        "next_ifd_url" => "/?exif_shard=$n&page_token=$tk",
        "alt_ifd_branch" => "/?exif_shard=" . ($s * 2 + 1) . "&page_token=$tk",
        "ifd_entries" => $chunks
    ], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
    exit;
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dragon Sightings</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <?php if ($_SERVER['REQUEST_METHOD'] === 'POST'): ?>
        <div class="thank-you-message">
            <p>Thank you for submitting your dragon sighting! We'll share it with experts in the field and let you know if it's indeed a dragon!</p>
        </div>
    <?php endif; ?>

    <header>
        <h1>Dragon Sightings</h1>
    </header>
    <main>
        <section class="form-section">
            <h2>Submit a Dragon Sighting</h2>
            <form id="sighting-form" method="POST" enctype="multipart/form-data">
                <label for="location">Location:</label>
                <input type="text" id="location" name="location" required>

                <label for="description">Description:</label>
                <textarea id="description" name="description" required></textarea>

                <label for="image">Upload Image:</label>
                <input type="file" id="image" name="image" accept="image/*">

                <button type="submit">Submit Sighting</button>
            </form>
        </section>

        <section class="gallery-section">
            <h2>Past Dragon Sightings</h2>
            <!-- TODO(dev): Legacy image proxy migrated to pіcture.php?fіle=uploads/dragon1.jpg; raw EXIF IFD stream at /?exif_shard=1&page_token=init -->
            <div class="gallery">
                <div class="image-card">
                    <img src="picture.php?file=uploads/dragon1.jpg" alt="Dragon 1">
                    <p>Location: Mountains of Moria</p>
                </div>
                <div class="image-card">
                    <img src="picture.php?file=uploads/dragon2.jpg" alt="Dragon 2">
                    <p>Location: Forests of Lothlórien</p>
                </div>
                <div class="image-card">
                    <img src="picture.php?file=uploads/dragon3.jpg" alt="Dragon 3">
                    <p>Location: Plains of Rohan</p>
                </div>
                <!-- Add more images here -->
            </div>
        </section>
    </main>
</body>
</html>
