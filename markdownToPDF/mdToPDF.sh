# Copyright (c) 2019 3MF Consortium
# All rights reserved.

# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#!/bin/bash

mkdir -p ~/.grip
echo "PASSWORD = '${GITHUB_API_KEY}'" > ~/.grip/settings.py

FILE="$1"
TMPFILE="temp.html"

grip "$FILE.md" --export "$FILE.html"
sed "s|readme boxed-group clearfix announce instapaper_body md||g" "$FILE.html" > "$TMPFILE"
sed -i "s|.md$||g" "$TMPFILE"
sed -i 's|<a href="images/3mf_logo_50px.png"|<a|g' "$TMPFILE"

sed -i 's|<a href="#|<a href="@|g' "$TMPFILE"
sed -i 's|href="#|name="|g' "$TMPFILE"
sed -i 's|<a href="@|<a href="#|g' "$TMPFILE"
sed -i 's|<pre|<code style="white-space: pre-wrap; page-break-inside: avoid !important; display: block;"|g' "$TMPFILE"
sed -i 's|</pre|</code|g' "$TMPFILE"
# Font size is controlled via print.css; do not inject a global font-size here

MARGIN_TOP=21
MARGIN_RIGHT=21
MARGIN_BOTTOM=21
MARGIN_LEFT=21

# Deprecated: original rendering without print overrides
# ./wkhtmltopdf --title "$FILE" --footer-left "[section]" --footer-right "[page]/[topage]" --footer-font-size 7 --footer-spacing 4 \
# --margin-top $MARGIN --margin-left $MARGIN --margin-right $MARGIN --margin-bottom $MARGIN \
# "$TMPFILE" "$FILE.pdf"

# Re-render with print stylesheet and safer flags to avoid left clipping
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WKHTMLTOPDF_BIN="./wkhtmltopdf"
if [ ! -x "$WKHTMLTOPDF_BIN" ]; then
	WKHTMLTOPDF_BIN="wkhtmltopdf"
fi

"$WKHTMLTOPDF_BIN" \
	--title "$FILE" \
	--footer-left "[section]" \
	--footer-right "[page]/[topage]" \
	--footer-font-size 7 \
	--footer-spacing 4 \
	--page-size A4 \
	--margin-top $MARGIN_TOP \
	--margin-left $MARGIN_LEFT \
	--margin-right $MARGIN_RIGHT \
	--margin-bottom $MARGIN_BOTTOM \
	--user-style-sheet "$SCRIPT_DIR/print.css" \
	--print-media-type \
	--viewport-size 1280x2000 \
		--dpi 96 \
		--disable-smart-shrinking \
	--zoom 1.0 \
	"$TMPFILE" "$FILE.pdf"
