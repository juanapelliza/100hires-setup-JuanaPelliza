import argparse
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
)


VIDEO_URL = "https://www.youtube.com/watch?v=R96I-v_06tI"
OUTPUT_FILE = Path("research/youtube-transcripts/sam-dunning-raw.txt")


def get_video_id(url: str) -> str:
    parsed = urlparse(url)
    video_id = parse_qs(parsed.query).get("v", [None])[0]
    if not video_id and parsed.netloc in {"youtu.be", "www.youtu.be"}:
        video_id = parsed.path.lstrip("/") or None
    if not video_id:
        raise ValueError(f"Could not extract video id from URL: {url}")
    return video_id


def fetch_transcript_lines(video_id: str) -> list[str]:
    transcript_data = YouTubeTranscriptApi().fetch(video_id, languages=["en"])
    return [entry.text.strip() for entry in transcript_data if entry.text.strip()]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract a YouTube transcript and save it to a text file."
    )
    parser.add_argument(
        "url",
        nargs="?",
        default=VIDEO_URL,
        help="YouTube video URL (defaults to the Sam Dunning video).",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=OUTPUT_FILE,
        help=(
            "Output path for transcript text "
            "(default: research/youtube-transcripts/sam-dunning-raw.txt)."
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    video_id = get_video_id(args.url)
    try:
        lines = fetch_transcript_lines(video_id)
    except (NoTranscriptFound, TranscriptsDisabled, VideoUnavailable) as exc:
        print(f"Could not fetch transcript for video id '{video_id}': {exc}")
        return

    output_file = args.output
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text("\n".join(lines), encoding="utf-8")

    print(f"Saved transcript to: {output_file}")
    print(f"Total lines: {len(lines)}")


if __name__ == "__main__":
    main()
