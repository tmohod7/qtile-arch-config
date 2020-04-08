# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget

from typing import List  # noqa: F401

mod = "mod4"

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn("termite")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),
]

##### COLORS #####
colors = [["#282a36", "#282a36"], # panel background
          ["#434758", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # background color for layout widget
          ["#A77AC4", "#A77AC4"], # dark green gradiant for other screen tabs
          ["#7197E7", "#7197E7"]] # background color for pacman widget

groups = [Group(i) for i in "12345678"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

layouts = [
    layout.Max(),
    layout.Stack(num_stacks=2)
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
            	widget.Sep(linewidth=0, padding=6, foreground=colors[2], background=colors[0]),
                widget.GroupBox(
                	font="Ubuntu Bold",
                	margin_y = 0,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 5,
                        borderwidth = 1,
                        active = colors[2],
                        inactive = colors[2], 
                	highlight_method = "block", 
                	fontsize=13,
                	this_current_screen_border = colors[4],
                        this_screen_border = colors [1],
                        other_current_screen_border = colors[0],
                        other_screen_border = colors[0],
                        foreground = colors[2],
                        background = colors[0]
                ),
                widget.Prompt(),
                widget.WindowName(font="Ubuntu Bold", 
                	fontsize=13, 
                	foreground=colors[4], 
                	background=colors[0], 
                	padding=5
                ),
                widget.Sep(linewidth=0, padding=6, foreground=colors[2], background=colors[0]),
                widget.TextBox(font="Ubuntu Bold",
                	text="", 
                	padding = 5, 
                	foreground=colors[2], 
                	background=colors[4], 
                	fontsize=14
                ),
                widget.Pacman(font="Ubuntu Bold",
                	execute = "alacritty", 
                	update_interval = 1800, 
                	foreground = colors[2], 
                	background = colors[4]
                ),
                widget.TextBox(font="Ubuntu Bold", text="Updates", padding = 5, foreground=colors[2], background=colors[4]),
                widget.TextBox(font="Ubuntu Bold",
                        text="",
                        foreground=colors[2],
                        background=colors[5],
                        padding = 5,
                        fontsize=14
                        ),
                widget.Memory(font="Ubuntu Bold",
                        foreground = colors[2],
                        background = colors[5],
                        padding = 5,
                        update_interval = 2.0
                        ),
                widget.DF(font="Ubuntu Bold",
                	format='({uf}{m} / {f}{m} - {r:.0f}%)',
                	padding = 5,
                	visible_on_warn = False,
                	foreground = colors[2],
                        background = colors[5]                	
                ),
                widget.TextBox(font="Ubuntu Bold",
                        text=" ♫",
                        padding = 5,
                        foreground=colors[2],
                        background=colors[4],
                        fontsize=14
                ),
                widget.Cmus(font="Ubuntu Bold",
                        max_chars = 40,
                        update_interval = 0.5,
                        background=colors[4],
                        play_color = colors[2],
                        noplay_color = colors[2]
                ),
                widget.TextBox(font="Ubuntu Bold",
                        text=" ",
                        foreground=colors[2],
                        background=colors[5],
                        padding = 5,
                        fontsize=14
                        ),
               	widget.Volume(font="Ubuntu Bold", 
                        foreground = colors[2],
                        background = colors[5],
                        padding = 10
                        ),
                widget.TextBox(font="Ubuntu Bold",
                        text=" ",
                        padding = 5,
                        foreground=colors[2],
                        background=colors[4],
                        fontsize=14
                        ),
                widget.CurrentLayout(font="Ubuntu Bold",
                        foreground = colors[2],
                        background = colors[4],
                        padding = 5
                        ),
                widget.TextBox(font="Ubuntu Bold",
                	text=" ",
                	padding = 5,
                	foreground=colors[2],
                	background=colors[5],
                	fontsize=14
                ),
                widget.Battery(font="Ubuntu Bold",
                	format="{char} {percent:2.0%}",
                	foreground=colors[2],
                	background=colors[5],
                	fontsize=14,
                	update_interval=5
                ),
                widget.TextBox(font="Ubuntu Bold",
                        text=" ",
                        foreground=colors[2],
                        background=colors[4],
                        padding = 5,
                        fontsize=14
                        ),
                widget.Clock(font="Ubuntu Bold",
                        foreground = colors[2],
                        background = colors[4],
                        format="%a %d %b %y - %I:%M %p"
                        ),
                widget.Systray(
                        background=colors[0],
                        padding = 5
                        ),
                widget.Sep(linewidth=0, padding=6, foreground=colors[2], background=colors[0]),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
