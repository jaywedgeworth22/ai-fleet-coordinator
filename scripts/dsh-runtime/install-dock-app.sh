#!/usr/bin/env bash
# Build ~/Applications/DeepSeek Harness Web.app and pin it to the Dock.
# Icon is a full-bleed 1:1 square (sharp 90° corners), not the official squircle.
set -euo pipefail
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$PATH"

ROOT="$(cd "$(dirname "$0")" && pwd)"
LIVE="${HOME}/apps/dsh-runtime"
APP="${HOME}/Applications/DeepSeek Harness Web.app"
PNG="${ROOT}/assets/harness-icon-1024.png"
[[ -f "$PNG" ]] || PNG="${LIVE}/assets/harness-icon-1024.png"

if [[ ! -f "$PNG" ]]; then
  echo "missing harness-icon-1024.png" >&2
  exit 1
fi
if [[ ! -x "${ROOT}/open-harness.sh" && ! -x "${LIVE}/open-harness.sh" ]]; then
  echo "missing open-harness.sh" >&2
  exit 1
fi

mkdir -p "${HOME}/Applications"
rm -rf "$APP"
mkdir -p "$APP/Contents/MacOS" "$APP/Contents/Resources"

OPEN_SRC="${ROOT}/open-harness.sh"
[[ -x "$OPEN_SRC" ]] || OPEN_SRC="${LIVE}/open-harness.sh"
cp "$OPEN_SRC" "$APP/Contents/MacOS/open-harness"
chmod 755 "$APP/Contents/MacOS/open-harness"

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
mkdir -p "$TMP/AppIcon.iconset"
for s in 16 32 128 256 512; do
  sips -z "$s" "$s" "$PNG" --out "$TMP/AppIcon.iconset/icon_${s}x${s}.png" >/dev/null
  sips -z "$((s * 2))" "$((s * 2))" "$PNG" --out "$TMP/AppIcon.iconset/icon_${s}x${s}@2x.png" >/dev/null
done
iconutil -c icns "$TMP/AppIcon.iconset" -o "$APP/Contents/Resources/AppIcon.icns"

cat > "$APP/Contents/Info.plist" <<'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>CFBundleDevelopmentRegion</key><string>en</string>
  <key>CFBundleDisplayName</key><string>DeepSeek Harness</string>
  <key>CFBundleExecutable</key><string>open-harness</string>
  <key>CFBundleIconFile</key><string>AppIcon</string>
  <key>CFBundleIdentifier</key><string>com.jays.dsh-harness-web</string>
  <key>CFBundleInfoDictionaryVersion</key><string>6.0</string>
  <key>CFBundleName</key><string>DeepSeek Harness</string>
  <key>CFBundlePackageType</key><string>APPL</string>
  <key>CFBundleShortVersionString</key><string>1.0</string>
  <key>CFBundleVersion</key><string>1</string>
  <key>LSMinimumSystemVersion</key><string>14.0</string>
  <key>LSUIElement</key><true/>
  <key>NSHighResolutionCapable</key><true/>
</dict>
</plist>
PLIST
echo -n "APPL????" > "$APP/Contents/PkgInfo"
codesign --force --deep -s - "$APP" >/dev/null 2>&1 || true

# Live copies so the app can also be rebuilt from ~/apps/dsh-runtime
mkdir -p "${LIVE}/assets"
cp "$OPEN_SRC" "${LIVE}/open-harness.sh"
chmod 755 "${LIVE}/open-harness.sh"
cp "$PNG" "${LIVE}/assets/harness-icon-1024.png"
cp "$ROOT/install-dock-app.sh" "${LIVE}/install-dock-app.sh" 2>/dev/null || true
chmod 755 "${LIVE}/install-dock-app.sh" 2>/dev/null || true

if command -v dockutil >/dev/null 2>&1; then
  if dockutil --list | grep -q "DeepSeek Harness Web"; then
    dockutil --remove "DeepSeek Harness Web" --no-restart || true
  fi
  if dockutil --list | awk -F'\t' '{print $1}' | grep -qx "DeepSeek"; then
    dockutil --add "$APP" --after "DeepSeek" --no-restart
  else
    dockutil --add "$APP" --no-restart
  fi
  killall Dock 2>/dev/null || true
else
  echo "dockutil not installed; app is at $APP — drag it to the Dock" >&2
fi

echo "installed $APP"
echo "opens ${DSH_WEB_URL:-http://127.0.0.1:3080/} via Chrome --app (no Terminal)"
