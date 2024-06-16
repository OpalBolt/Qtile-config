#! /bin/bash
# Most of this script is stolen directly from:https://github.com/vivien/i3blocks-contrib/blob/master/volume-pulseaudio/volume-pulseaudio
# One other command is from: https://github.com/wingej0/dotfiles/blob/98b3d0db7ebaf838bf046e693bf01aa3b51e183e/qtile/scripts/volume.sh

AUDIO_DELTA=${AUDIO_DELTA:-5}
MIXER=${MIXER:-""}
SCONTROL=${SCONTROL:-""}

if [[ -z "$MIXER" ]]; then
	MIXER="default"
	if amixer -D pulse info >/dev/null 2>&1; then
		MIXER="pulse"
	fi
fi

if [[ -z "$SCONTROL" ]]; then
	SCONTROL=$(amixer -D "$MIXER" scontrols | sed -n "s/Simple mixer control '\([^']*\)',0/\1/p" | head -n1)
fi

CAPABILITY=$(amixer -D $MIXER get $SCONTROL | sed -n "s/  Capabilities:.*cvolume.*/Capture/p")

function move_sinks_to_new_default {
	DEFAULT_SINK=$1
	pactl list sink-inputs | grep 'Sink Input #' | grep -o '[0-9]\+' | while read SINK; do
		pactl move-sink-input $SINK $DEFAULT_SINK
	done
}

function set_default_playback_device_next {
	inc=${1:-1}
	num_devices=$(pactl list sinks | grep -c Name:)
	sink_arr=($(pactl list sinks | grep Name: | sed -r 's/\s+Name: (.+)/\1/'))
	default_sink=$(pactl get-default-sink)
	default_sink_index=$(for i in "${!sink_arr[@]}"; do if [[ "$default_sink" = "${sink_arr[$i]}" ]]; then echo "$i"; fi; done)
	default_sink_index=$((($default_sink_index + $num_devices + $inc) % $num_devices))
	default_sink=${sink_arr[$default_sink_index]}
	pactl set-default-sink $default_sink
	move_sinks_to_new_default $default_sink
}

case $1 in
1) set_default_playback_device_next ;;
2) amixer -q -D $MIXER sset $SCONTROL $CAPABILITY toggle ;;
3) set_default_playback_device_next -1 ;;
4) amixer -q -D $MIXER sset $SCONTROL $CAPABILITY $AUDIO_DELTA%+ ;;
5) amixer -q -D $MIXER sset $SCONTROL $CAPABILITY $AUDIO_DELTA%- ;;
*) echo $(wpctl get-volume @DEFAULT_AUDIO_SINK@ | awk '{v = $2; print (v*100)"%"}') ;;
esac
